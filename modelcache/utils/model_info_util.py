# -*- coding: utf-8 -*-
import json
from modelcache import cache
from modelcache.utils.collection_util import get_collection_iat_name


def model_version_save(scope):
    model = scope.get('model')
    sorted_dict = dict(sorted(scope.items(), key=lambda x: x[0]))
    hyper_param_str = json.dumps(sorted_dict)
    # query from db
    resp = cache.data_manager.query_model_max_version(model)
    max_version = resp[0]
    if max_version is None:
        version = 1
    else:
        version = max_version+1
    # write to db
    cache.data_manager.save_model_info(hyper_param_str, model, version)
    return version


def model_partition_save(model, system_prompt):
    resp = cache.data_manager.query_model_max_partition(model)
    max_version = resp[0]
    if max_version is None:
        version = 1
    else:
        version = max_version+1
    # write to ob
    resp = cache.data_manager.save_model_partitio_info(system_prompt, model, version)
    print('insert_resp: {}'.format(resp))
    return version
