# Parameterization settings. These will be explained in 2.2. Now simply copy them to run the test.
export ROUTES=${LEADERBOARD_ROOT}/data/routes_devtest.xml
# export ROUTES=${LEADERBOARD_ROOT}/data/routes_custom.xml
export REPETITIONS=1
export DEBUG_CHALLENGE=1
# export TEAM_AGENT=${LEADERBOARD_ROOT}/leaderboard/autoagents/human_agent.py
# export TEAM_AGENT=${LEADERBOARD_ROOT}/leaderboard/autoagents/dummy_agent.py
# export TEAM_AGENT=${LEADERBOARD_ROOT}/leaderboard/autoagents/npc_agent.py
export TEAM_AGENT=${TEAM_CODE_ROOT}/npc_agent.py
# export TEAM_AGENT=${TEAM_CODE_ROOT}/0sensor.py
export CHECKPOINT_ENDPOINT=${LEADERBOARD_ROOT}/results.json
export CHALLENGE_TRACK_CODENAME=SENSORS
# export CHALLENGE_TRACK_CODENAME=MAP

./scripts/run_evaluation.sh