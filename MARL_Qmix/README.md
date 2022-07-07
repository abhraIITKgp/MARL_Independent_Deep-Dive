# June 30 Update

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



# June 29 Update on using UMIACS Clusters

First basics on using SCP to transfer files from local machine to UMIACS remote. Use `-r` flag to transfer entire folder.

```
scp /path/to/local/source user@cmlsub00.umiacs.umd.edu:/path/to/remote/destination 
scp -r /path/to/local/source_dir user@cmlsub00.umiacs.umd.edu:/path/to/remote/destination 
```

I have made a shell script `run_qmix.sh` that is used for running `sbatch` command. Change the content inside the shell script to change what program to run.

SSH into UMIACS, `cd` to the directory where the program is stored, use `sbatch` command to run program on clusters.

Using CPU nodes (GPU may not be available):
```
sbatch --partition=cpu --qos=cpu run_qmix.sh
```

# June 16 Update

## Virtual Environment Setup

Following https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html to install and set up conda. I set `auto_activate_base` to false so that it doesn't activate everytime I open my machine.
```
conda config --set auto_activate_base false
```

Then start setting up a test virtual environment
```
conda init
conda create -n marl-test python=3.9
conda activate marl-test
```

Good thing about using virtual environment is that you can keep different work that relies on different dependencies in separate environment. This would be helpful as project grows large.

Now I can start testing the many MARL environments.

## Gym

Simply install and test via:
```
pip install gym
python3 gym_test.py
```

## PettingZoo 

Simply install via:
```
pip install pettingzoo
```

I followed https://towardsdatascience.com/multi-agent-deep-reinforcement-learning-in-15-lines-of-code-using-pettingzoo-e0b963c0820b to replicate a simple game of Piston. To start, it first need other libraries. This example also uses SuperSuit wrapper. 
```
pip install stable-baselines3[extra]
pip install SuperSuit
pip install pygame
pip install pymunk
```

Then we can train and save a basic PistonBall game (warnings can be ignored for now). This may take a while to run.
```
python3 pettingzoo_test.py
```

We can watch the result (need GUI)
```
python3 pettingzoo_vis.py
```

Author: Chenqi "Matthew" Zhu
