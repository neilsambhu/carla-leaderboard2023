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
