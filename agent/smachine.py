class smachine:
	def __init__(self, state, states:dict):
		self.states = states
		self.state = state
	def getS(self):
		return self.state
	def doEvent(self, someEvent):
		if (self.states[self.state][someEvent]):
 			self.state = self.states[self.state][someEvent]

### example usage: 
# somestates = {
# 	"red": {
#     	"time_elapsed_red": "green",
#         "firetruck": "green",
#     },
# 	"green": {
# 		"time_elapsed_green": "solid yellow"
#         },
# 	"solid yellow" : {
#     	"time_elapsed_solid_yellow": "blinking yellow",
#         "firetruck": "green",
#         },
# 	"blinking yellow": {
#     	"time_elapsed_blinking_yellow": "red",
#         "firetruck": "green",
# 	}
# }

# trafficlight = smachine("green", somestates)
# print(trafficlight.getS())  # output: green
# trafficlight.doEvent("time_elapsed_green")
# print(trafficlight.getS()) # output: solid yellow
# trafficlight.doEvent("time_elapsed_solid_yellow")
# print(trafficlight.getS()) # output: blinking yellow
# trafficlight.doEvent("time_elapsed_blinking_yellow")
# print(trafficlight.getS()) # output: red
# trafficlight.doEvent("time_elapsed_red")
# print(trafficlight.getS()) # output: green
# trafficlight.doEvent("time_elapsed_green")
# print(trafficlight.getS()) # output: solid yellow
# trafficlight.doEvent("time_elapsed_solid_yellow")
# print(trafficlight.getS()) # output: blinking yellow
# trafficlight.doEvent("firetruck")
# print(trafficlight.getS()) # output: back to green because a fire truck must run the light