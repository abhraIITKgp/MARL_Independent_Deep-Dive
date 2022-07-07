## Installation and Env setup guide

To run QMIX from https://github.com/quantumiracle/Popular-RL-Algorithms/blob/master/qmix.py a few changes have to be made.

First make sure pettingzoo and SuperSuit are of specific versions and install required libraries. (Their requirements.txt doesn't work)
```
pip install pettingzoo==1.18.1
pip install SuperSuit==3.4.0
pip install multi-agent-ale-py
pip install autorom
```

Also comment out line 21 and 22 from `common/wrappers.py` as those variables are not used but cause errors.

Run with train flag to train and test flag to evaluate, change to `max_steps` and `max_episodes` flag to toggle the training/testing iterations.

Use flag `-s` to specify the `max` or `min` training situation for the two agents.

Use flag `--verbose` to print out Rewards and Loss for each episode as the program run.

```
python3 qmix.py --train --max_steps 500 --max_episodes 1000 -s max min
python3 qmix.py --test --max_episodes 10
```

Author: Abhranil Chandra
