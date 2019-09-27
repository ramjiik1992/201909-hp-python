import logging
import os
format='%(asctime)s\t[%(levelname)s]\t%(message)s'
logging.basicConfig(format=format,level=logging.WARN)

log = logging.getLogger(__name__)
 
log.debug('debug')
log.info('info')
log.warn('warn')
log.error('error')
log.critical('critical')