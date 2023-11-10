import hydra
from omegaconf import DictConfig, OmegaConf
import logging


logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path='config', config_name='config')
def main(cfg: DictConfig) -> None:
    cfg_yaml = OmegaConf.to_yaml(cfg, resolve=True)
    
    logger.info(f"Config:\n{cfg_yaml}")
    

if __name__ == "__main__":
    main()