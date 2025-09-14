#!/usr/bin/env python3
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any

class QuickMemory:
    def __init__(self, storage_file: str = "memory.json"):
        self.storage_file = storage_file
        self.memory = self._load()
    
    def _load(self) -> Dict:
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def _agent_key(self, agent: str, key: str) -> str:
        """Create namespaced key: agent.key"""
        return f"{agent}.{key}"
    
    def set(self, key: str, value: Any, agent: str = "default"):
        """Set a value for an agent: mem.set('tasks.urgent', [...], 'essay_bot')"""
        full_key = self._agent_key(agent, key)
        self.memory[full_key] = value
        self.save()
    
    def get(self, key: str, default=None, agent: str = "default"):
        """Get a value for an agent: mem.get('tasks.urgent', agent='essay_bot')"""
        full_key = self._agent_key(agent, key)
        return self.memory.get(full_key, default)
    
    def append(self, key: str, item: Any, agent: str = "default"):
        """Append to an agent's list"""
        full_key = self._agent_key(agent, key)
        if full_key not in self.memory:
            self.memory[full_key] = []
        if isinstance(self.memory[full_key], list):
            self.memory[full_key].append(item)
            self.save()
        else:
            raise ValueError(f"Key {full_key} is not a list")
    
    def remove(self, key: str, item: Any = None, agent: str = "default"):
        """Remove item from agent's list or delete key entirely"""
        full_key = self._agent_key(agent, key)
        if item is None:
            if full_key in self.memory:
                del self.memory[full_key]
                self.save()
        else:
            if full_key in self.memory and isinstance(self.memory[full_key], list):
                try:
                    self.memory[full_key].remove(item)
                    self.save()
                except ValueError:
                    pass
    
    def wipe_agent(self, agent: str):
        """Delete all memories for an agent"""
        prefix = f"{agent}."
        keys_to_delete = [k for k in self.memory.keys() if k.startswith(prefix)]
        for key in keys_to_delete:
            del self.memory[key]
        self.save()
        return f"Wiped {len(keys_to_delete)} memories for agent '{agent}'"
    
    def list_agents(self) -> List[str]:
        """List all agents that have memories"""
        agents = set()
        for key in self.memory.keys():
            if '.' in key:
                agent = key.split('.', 1)[0]
                agents.add(agent)
        return sorted(list(agents))
    
    def list_keys(self, prefix: str = "", agent: str = None) -> List[str]:
        """List keys, optionally filtered by prefix and/or agent"""
        if agent:
            agent_prefix = f"{agent}."
            keys = [k[len(agent_prefix):] for k in self.memory.keys() 
                   if k.startswith(agent_prefix)]
        else:
            keys = list(self.memory.keys())
        
        if prefix:
            keys = [k for k in keys if k.startswith(prefix)]
        return keys
    
    def show(self, prefix: str = "", agent: str = None) -> str:
        """Pretty print memories, optionally for specific agent"""
        if agent:
            agent_prefix = f"{agent}."
            keys = [k for k in self.memory.keys() if k.startswith(agent_prefix)]
            display_keys = {k: k[len(agent_prefix):] for k in keys}
        else:
            keys = self.memory.keys()
            display_keys = {k: k for k in keys}
        
        if prefix:
            keys = [k for k in keys if display_keys[k].startswith(prefix)]
        
        result = []
        if agent:
            result.append(f"=== Agent: {agent} ===")
        
        for key in sorted(keys):
            display_key = display_keys[key]
            value = self.memory[key]
            if isinstance(value, list):
                result.append(f"{display_key}:")
                for i, item in enumerate(value, 1):
                    result.append(f"  {i}. {item}")
            else:
                result.append(f"{display_key}: {value}")
        return ('\n').join(result)