# Course 2: Memory Systems & Agent Architectures
**Duration**: 8-10 weeks (1 hour/day)  
**Prerequisites**: Course 1 completion  
**Goal**: Build sophisticated memory systems and understand agent-based cognitive architectures

*Curriculum developed in collaboration with Claude (Anthropic) - AI-assisted course design and resource curation*

## Week 1: Memory Systems Fundamentals
**Objective**: Understand different types of memory and their computational implementations

### Day 1-2: Human Memory Models
- **Study**: [Working Memory Model](https://www.simplypsychology.org/working%20memory.html)
- **Study**: [Long-term Memory Types](https://www.verywellmind.com/what-is-long-term-memory-2795347)
- **Project**: Design a conceptual model of your synthetic person's memory architecture

### Day 3-4: Neural Memory Mechanisms
- **Study**: [Memory Networks](https://arxiv.org/abs/1410.3916) - Sections 1-3
- **Study**: [Differentiable Neural Computers](https://deepmind.com/blog/article/differentiable-neural-computers) (blog post)
- **Project**: Implement simple associative memory using neural networks

### Day 5-7: Attention Mechanisms
- **Study**: [Attention is All You Need](https://arxiv.org/abs/1706.03762) - Focus on attention mechanism
- **Study**: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- **Project**: Build attention mechanism from scratch, test on sequence data

## Week 2: Working Memory Implementation
**Objective**: Create functional working memory systems

### Day 8-10: Short-term Memory Buffers
- **Study**: [LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- **Practice**: Implement LSTM from scratch
- **Project**: Build short-term memory buffer with capacity limits and decay

### Day 11-14: Episodic Memory Systems
- **Study**: [Episodic Memory in Deep Learning](https://arxiv.org/abs/1703.01988)
- **Study**: [Memory-Augmented Neural Networks](https://arxiv.org/abs/1605.06065)
- **Project**: Create episodic memory system that stores and retrieves experiences

## Week 3: Long-term Memory & Knowledge Representation
**Objective**: Build persistent knowledge storage and retrieval systems

### Day 15-17: Semantic Memory
- **Study**: [Knowledge Graphs](https://www.ontotext.com/knowledgehub/fundamentals/what-is-a-knowledge-graph/)
- **Study**: [Graph Neural Networks](https://distill.pub/2021/gnn-intro/)
- **Project**: Build semantic memory using graph structures

### Day 18-21: Memory Consolidation
- **Study**: [Complementary Learning Systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4724297/)
- **Study**: [Catastrophic Forgetting](https://www.pnas.org/doi/10.1073/pnas.1611835114)
- **Project**: Implement memory consolidation mechanism

## Week 4: Agent Architectures
**Objective**: Understand different approaches to building intelligent agents

### Day 22-24: Reactive Agents
- **Study**: [Behavior-Based Robotics](https://www.cs.cmu.edu/~./15381/lectures/lecture02.pdf)
- **Study**: [Subsumption Architecture](https://people.cs.umass.edu/~grupen/503/papers/brooks86.pdf)
- **Project**: Build reactive agent for simple environment

### Day 25-28: Deliberative Agents
- **Study**: [BDI Architecture](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/imas/IMAS2e-Ch02.pdf)
- **Study**: [SOAR Cognitive Architecture](https://soar.eecs.umich.edu/articles/articles/soar-tutorial/78)
- **Project**: Implement simple BDI agent with beliefs, desires, intentions

## Week 5: Hybrid Cognitive Architectures
**Objective**: Combine reactive and deliberative approaches

### Day 29-31: Layered Architectures
- **Study**: [Three-Layer Architecture](https://www.sciencedirect.com/science/article/pii/S0004370296000094)
- **Study**: [CLARION Architecture](https://www.cogsci.rpi.edu/~rsun/clarion-tut.pdf)
- **Project**: Build three-layer agent (reactive, executive, deliberative)

### Day 32-35: Integration Mechanisms
- **Study**: [Cognitive Architectures Comparison](https://www.aaai.org/Papers/AAAI/2008/AAAI08-167.pdf)
- **Practice**: Compare different integration approaches
- **Project**: Design integration mechanism for your synthetic person

## Week 6: Planning & Goal Management
**Objective**: Implement sophisticated planning and goal-oriented behavior

### Day 36-38: Goal Hierarchies
- **Study**: [Hierarchical Planning](https://www.cs.cmu.edu/~./15381/lectures/lecture07.pdf)
- **Study**: [Goal Networks](https://arxiv.org/abs/1704.06567)
- **Project**: Build hierarchical goal management system

### Day 39-42: Dynamic Planning
- **Study**: [Real-time Planning](https://www.cs.cmu.edu/~./15381/lectures/lecture08.pdf)
- **Study**: [Monte Carlo Tree Search](https://www.nature.com/articles/nature16961)
- **Project**: Implement dynamic planning with replanning capabilities

## Week 7: Learning & Adaptation
**Objective**: Add learning capabilities to agent systems

### Day 43-45: Experience-based Learning
- **Study**: [Reinforcement Learning Basics](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) - Chapters 1-3
- **Study**: [Q-Learning](https://link.springer.com/article/10.1007/BF00992698)
- **Project**: Add Q-learning to your agent

### Day 46-49: Meta-Learning
- **Study**: [Learning to Learn](https://arxiv.org/abs/1606.04474)
- **Study**: [Model-Agnostic Meta-Learning](https://arxiv.org/abs/1703.03400)
- **Project**: Implement simple meta-learning for your agent

## Week 8: Multi-Modal Processing
**Objective**: Integrate multiple sensory modalities

### Day 50-52: Vision-Language Integration
- **Study**: [CLIP](https://openai.com/blog/clip/) - Connecting text and images
- **Study**: [Multimodal Deep Learning](https://arxiv.org/abs/1705.09406)
- **Project**: Build simple vision-language understanding system

### Day 53-56: Sensor Fusion
- **Study**: [Sensor Fusion Techniques](https://www.researchgate.net/publication/330776097_Sensor_Fusion_Techniques_for_Autonomous_Driving)
- **Practice**: Combine different data modalities
- **Project**: Create multi-modal perception system

## Week 9-10: Integration Project
**Objective**: Build complete agent with memory and multi-modal capabilities

### Day 57-63: System Integration
- **Project**: Combine all components into unified agent
- **Testing**: Evaluate agent performance on complex tasks
- **Documentation**: Document architecture and design decisions

### Day 64-70: Advanced Features
- **Project**: Add advanced features (creativity, emotion, self-reflection)
- **Evaluation**: Test agent in various scenarios
- **Presentation**: Prepare demonstration of capabilities

## Resources & Tools

### Essential Libraries
- **Memory**: PyTorch, NumPy, NetworkX (for graphs)
- **Planning**: PDDL parsers, planning libraries
- **Multi-modal**: OpenCV, PIL, speech recognition libraries
- **Visualization**: Matplotlib, Plotly, Graphviz

### Key Papers & Resources
- **Memory**: "Memory Networks", "Differentiable Neural Computers"
- **Agents**: "Artificial Intelligence: A Modern Approach" - Chapters 2-4
- **Planning**: "Automated Planning: Theory and Practice"
- **Multi-modal**: Recent vision-language model papers

### Development Tools
- **Environment**: Jupyter notebooks, VS Code
- **Simulation**: OpenAI Gym, custom environments
- **Debugging**: TensorBoard, custom visualization tools

## Assessment & Milestones

### Week 3 Checkpoint
- Working memory system with attention mechanisms
- Episodic and semantic memory implementation

### Week 6 Checkpoint
- Complete agent architecture with planning
- Goal-oriented behavior demonstration

### Final Project
- Integrated agent with memory, planning, and multi-modal processing
- Demonstration of learning and adaptation
- Documentation of architecture and capabilities

## Preparation for Course 3
By the end of this course, you should be ready to tackle:
- Emotional and motivational systems
- Creativity and imagination
- Self-reflection and metacognition
- Advanced human-AI interaction

## Daily Schedule Template
- **10 min**: Review and connect to previous concepts
- **35 min**: New material study and implementation
- **15 min**: Integration with existing project

## Success Indicators
- Can design and implement different memory architectures
- Understands trade-offs between different agent approaches
- Can integrate multiple systems into coherent architecture
- Demonstrates learning and adaptation in agent behavior
- Can explain design decisions and architectural choices

## Extension Projects
- Build agent for specific domain (game playing, conversation, etc.)
- Implement advanced memory mechanisms (attention, consolidation)
- Add emotional and motivational components
- Create multi-agent interactions