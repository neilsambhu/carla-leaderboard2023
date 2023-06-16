# carla-leaderboard2023
6/8/2023 1:30:00 PM: TODO: see high-level command in npc_agent.py.  
6/8/2023 1:34:51 PM: find RoadOption.  
```
grep -r -e "RoadOption." |& tee outgrep.txt
```
6/8/2023 1:47:40 PM: outgrep results
```
leaderboard/scenarios/route_scenario.py:            if w[1] == RoadOption.LEFT:  # Yellow
leaderboard/scenarios/route_scenario.py:            elif w[1] == RoadOption.RIGHT:  # Cyan
leaderboard/scenarios/route_scenario.py:            elif w[1] == RoadOption.CHANGELANELEFT:  # Orange
leaderboard/scenarios/route_scenario.py:            elif w[1] == RoadOption.CHANGELANERIGHT:  # Dark Cyan
leaderboard/scenarios/route_scenario.py:            elif w[1] == RoadOption.STRAIGHT:  # Gray
Binary file leaderboard/scenarios/__pycache__/route_scenario.cpython-37.pyc matches
Binary file leaderboard/utils/__pycache__/route_manipulation.cpython-37.pyc matches
Binary file leaderboard/utils/__pycache__/route_parser.cpython-37.pyc matches
leaderboard/utils/route_manipulation.py:        elif curr_option in (RoadOption.CHANGELANELEFT, RoadOption.CHANGELANERIGHT):
leaderboard/utils/route_manipulation.py:        elif prev_option != curr_option and prev_option not in (RoadOption.CHANGELANELEFT, RoadOption.CHANGELANERIGHT):
scripts/route_displayer.py:        if option == RoadOption.LEFT:  # Yellow
scripts/route_displayer.py:        elif option == RoadOption.RIGHT:  # Cyan
scripts/route_displayer.py:        elif option == RoadOption.CHANGELANELEFT:  # Orange
scripts/route_displayer.py:        elif option == RoadOption.CHANGELANERIGHT:  # Dark Cyan
scripts/route_displayer.py:        elif option == RoadOption.STRAIGHT:  # Gray
scripts/route_creator.py:from agents.navigation.local_planner import RoadOption
scripts/route_creator.py:    if option == RoadOption.LEFT:  # Yellow
scripts/route_creator.py:    elif option == RoadOption.RIGHT:  # Cyan
scripts/route_creator.py:    elif option == RoadOption.CHANGELANELEFT:  # Orange
scripts/route_creator.py:    elif option == RoadOption.CHANGELANERIGHT:  # Dark Cyan
scripts/route_creator.py:    elif option == RoadOption.STRAIGHT:  # Gray
```
6/8/2023 3:57:02 PM: find training code:
```
grep -r --exclude outgrep.txt -e "train" > outgrep.txt
```
6/8/2023 6:04:33 PM: TODO: how do I move forward with the end objective being to use the routes_training.xml?  
## InterFuser
6/9/2023 3:15 PM: grep "endpoint"
```
grep -r --exclude outgrep.txt -e "endpoint" |& tee outgrep.txt
```
6/9/2023 3:28 PM: error message 
```
(interfuser) nsambhu@SAMBHU19:~/github/InterFuser$ CUDA_VISIBLE_DEVICES=0 ./leaderboard/scripts/run_evaluation.sh
Traceback (most recent call last):
  File "leaderboard/leaderboard/leaderboard_evaluator.py", line 489, in <module>
    main()
  File "leaderboard/leaderboard/leaderboard_evaluator.py", line 476, in main
    statistics_manager = StatisticsManager()
TypeError: __init__() missing 2 required positional arguments: 'endpoint' and 'debug_endpoint'
```
6/9/2023 3:49 PM: set ~/.bashrc to InterFuser paths
```
(interfuser) nsambhu@SAMBHU19:~/github/InterFuser$ CUDA_VISIBLE_DEVICES=0 ./leaderboard/scripts/run_evaluation.sh
Traceback (most recent call last):
  File "leaderboard/leaderboard/leaderboard_evaluator.py", line 34, in <module>
    from leaderboard.scenarios.scenario_manager import ScenarioManager
  File "/home/nsambhu/github/InterFuser/leaderboard/leaderboard/scenarios/scenario_manager.py", line 25, in <module>
    from leaderboard.autoagents.agent_wrapper import AgentWrapper, AgentError
  File "/home/nsambhu/github/InterFuser/leaderboard/leaderboard/autoagents/agent_wrapper.py", line 21, in <module>
    from leaderboard.autoagents.autonomous_agent import Track
  File "/home/nsambhu/github/InterFuser/leaderboard/leaderboard/autoagents/autonomous_agent.py", line 17, in <module>
    from leaderboard.utils.route_manipulation import downsample_route
  File "/home/nsambhu/github/InterFuser/leaderboard/leaderboard/utils/route_manipulation.py", line 17, in <module>
    from agents.navigation.global_route_planner_dao import GlobalRoutePlannerDAO
ModuleNotFoundError: No module named 'agents.navigation.global_route_planner_dao'
```
6/9/2023 6:17:47 PM: grep sensor data
```
grep -r --exclude outgrep.txt -e "sensors" |& tee outgrep.txt
```
6/9/2023 6:25:22 PM: grep sensor rgb data
```
grep -r --exclude outgrep.txt -e "sensor.camera.rgb" |& tee outgrep.txt
```
6/10/2023 11:29:20 AM: InterFuser results Town05
```
(interfuser) nsambhu@SAMBHU19:~/github/InterFuser$ ./leaderboard/scripts/run_evaluation.sh
========= Preparing RouteScenario_16 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_17_26_05
> Loading the world
load
load
load
load
load
load
load
Skipping scenario 'Scenario4' due to setup error: list index out of range
> Running the route
> Stopping the route

========= Results of RouteScenario_16 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 17:29:16 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 18:34:37 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3921.19s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 917.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.234               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 89.97 % │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics
ERROR: failed to destroy actor 321 : unable to destroy actor: not found 
ERROR: failed to destroy actor 338 : unable to destroy actor: not found 
ERROR: failed to destroy actor 351 : unable to destroy actor: not found 
ERROR: failed to destroy actor 378 : unable to destroy actor: not found 
ERROR: failed to destroy actor 398 : unable to destroy actor: not found 

========= Preparing RouteScenario_17 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_18_34_38
> Loading the world
load
load
load
load
load
load
load
> Running the route
ERROR: failed to destroy actor 568 : unable to destroy actor: not found 
ERROR: failed to destroy actor 543 : unable to destroy actor: not found 
> Stopping the route

========= Results of RouteScenario_17 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 18:37:03 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 19:29:50 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3166.63s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 714.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.225               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 94.7 %  │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_18 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_19_29_51
> Loading the world
load
load
load
load
load
load
load
> Running the route
/home/nsambhu/github/InterFuser/leaderboard/team_code/tracker.py:141: RuntimeWarning: divide by zero encountered in double_scalars
  speed = 0.5 * self.frequency * np.sqrt((prev_pos[0]-cur_pos[0])**2+(prev_pos[1]-cur_pos[1])**2) / (to.historical_steps[i+1]-to.historical_steps[i])
> Stopping the route

========= Results of RouteScenario_18 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 19:32:38 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 20:32:01 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3563.04s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 846.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.237               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 90.99 % │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_19 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_20_32_02
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_19 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 20:36:18 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 21:03:12 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 1613.9s             │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 437.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.271               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ SUCCESS │ 100 %   │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ SUCCESS │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_20 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_21_03_13
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_20 (repetition 0) ------ SUCCESS =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 21:06:42 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 22:09:19 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3756.88s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 900.5s              │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.24                │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ SUCCESS │ 100 %   │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ SUCCESS │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_21 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_22_09_20
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_21 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 22:10:57 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 22:35:16 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 1458.79s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 346.8s              │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.238               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ SUCCESS │ 100 %   │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ SUCCESS │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_22 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_22_35_17
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_22 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 22:38:07 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-09 23:37:56 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3589.41s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 851.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.237               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 14.45 % │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_23 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_09_23_37_58
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_23 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-09 23:41:38 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-10 00:42:37 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 3658.79s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 840.05s             │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.23                │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ SUCCESS │ 100 %   │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 2 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ SUCCESS │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics

========= Preparing RouteScenario_24 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_10_00_42_38
> Loading the world
load
load
load
load
load
load
load
Skipping scenario 'Scenario4' due to setup error: list index out of range
> Running the route
ERROR: failed to destroy actor 2860 : unable to destroy actor: not found 
> Stopping the route

========= Results of RouteScenario_24 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-10 00:48:35 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-10 02:54:02 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 7527.01s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 1792.05s            │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.238               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 44.8 %  │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 2 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics
ERROR: failed to destroy actor 2887 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2888 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2889 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2891 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2893 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2897 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2899 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2900 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2901 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2902 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2904 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2905 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2906 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2907 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2910 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2917 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2918 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2919 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2920 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2926 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2929 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2930 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2933 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2934 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2937 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2938 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2939 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2940 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2941 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2942 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2943 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2944 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2945 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2946 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2947 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2951 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2952 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2953 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2954 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2955 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2956 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2957 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2959 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2960 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2963 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2964 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2966 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2967 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2971 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2972 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2973 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2975 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2977 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2978 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2980 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2983 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2985 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2986 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2988 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2990 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2991 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2994 : unable to destroy actor: not found 
ERROR: failed to destroy actor 2996 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3000 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3001 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3002 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3003 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3004 : unable to destroy actor: not found 
ERROR: failed to destroy actor 3005 : unable to destroy actor: not found 

========= Preparing RouteScenario_25 (repetition 0) =========
> Setting up the agent
load model: leaderboard/team_code/interfuser.pth.tar
routes_town05_long_06_10_02_54_04
> Loading the world
load
load
load
load
load
load
load
> Running the route
> Stopping the route

========= Results of RouteScenario_25 (repetition 0) ------ FAILURE =========

╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2023-06-10 02:58:29 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2023-06-10 04:30:40 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 5531.24s            │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 1321.05s            │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 0.239               │
╘═════════════════════════════════╧═════════════════════╛

╒═══════════════════════╤═════════╤═════════╕
│ Criterion             │ Result  │ Value   │
├───────────────────────┼─────────┼─────────┤
│ RouteCompletionTest   │ FAILURE │ 98.85 % │
├───────────────────────┼─────────┼─────────┤
│ OutsideRouteLanesTest │ SUCCESS │ 0 %     │
├───────────────────────┼─────────┼─────────┤
│ CollisionTest         │ FAILURE │ 1 times │
├───────────────────────┼─────────┼─────────┤
│ RunningRedLightTest   │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ RunningStopTest       │ SUCCESS │ 0 times │
├───────────────────────┼─────────┼─────────┤
│ InRouteTest           │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ AgentBlockedTest      │ SUCCESS │         │
├───────────────────────┼─────────┼─────────┤
│ Timeout               │ FAILURE │         │
╘═══════════════════════╧═════════╧═════════╛

> Registering the route statistics
> Registering the global statistics
```
6/12/2023 2:59 PM: test_run.sh is successful. grep rgb sensor data.
```
grep -r --exclude outgrep.txt -e "sensor.camera.rgb" |& tee outgrep.txt
```
6/12/2023 3:08 PM: find calls to npc_agent.py > sensors() method
```
grep -r --exclude outgrep.txt -e "sensors()" |& tee outgrep.txt
```
```
leaderboard/autoagents/agent_wrapper.py:        for sensor_spec in self._agent.sensors():
leaderboard/autoagents/agent_wrapper.py:        for sensor_spec in self._agent.sensors():
leaderboard/leaderboard_evaluator.py:                self.sensors = self.agent_instance.sensors()
```
6/12/2023 3:08 PM: find calls to ".sensors"
```
grep -r --exclude outgrep.txt -e ".sensors" |& tee outgrep.txt
```
6/12/2023 7:42:46 PM: find calls to "NPCAgent"
```
grep -r --exclude outgrep.txt -e "NpcAgent" |& tee outgrep.txt
```
6/13/2023 4:16 PM: RGB image data saved to hard disk. TODO: output vehicle control signal.  
6/14/2023 5:00 PM: find "sensor"
```
grep -r --exclude outgrep.txt -e "sensor" |& tee outgrep.txt
```
6/16/2023 3:46 PM: leaderboard_evaluator.py has self.sensors. Find calls to LeaderboardEvaluator.  
```
grep -r --exclude outgrep.txt -e "LeaderboardEvaluator" |& tee outgrep.txt
```
6/16/2023 3:54 PM: find ".sensor"
```
grep -F -r --exclude outgrep.txt -e ".sensor" |& tee outgrep.txt
```
