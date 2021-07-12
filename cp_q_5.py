from config import BASE_PATH, ALICE_BASE_PATH, Envs, EncType
from parallelize import parallelize_cp_q


hyperparams = {
    'episodes': [5000],
    'batch_size': [16],
    'epsilon': [1],
    'epsilon_decay': [0.99],
    'epsilon_min': [0.01],
    'gamma': [0.99],
    'update_after': [10],
    'update_target_after': [30],
    'learning_rate': [0.001],
    'learning_rate_in': [0.001],
    'learning_rate_out': [0.1],
    'circuit_depth': [15],
    'epsilon_schedule': ['fast'],
    'reps': 10,
    'env': Envs.CARTPOLE,
    'save': True,
    'test': False
}


if __name__ == '__main__':
    parallelize_cp_q(hyperparams, BASE_PATH + 'cartpole/depth_10/')
