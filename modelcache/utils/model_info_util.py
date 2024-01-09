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


def get_model_partition_formal(system_prompt, model, query_list, partition_info_dict):
    system_content = None
    res_list = list()
    for content_dict in query_list:
        role = content_dict['role']
        if role == 'system':
            system_content = content_dict['content']
        else:
            res_list.append(content_dict)

    model_system_key = model + '_' + system_content
    if model_system_key not in partition_info_dict:
        partition_version = model_partition_save(model, system_prompt)
        partition_info_dict[model_system_key] = partition_version
        return {'partition_version': partition_version, 'query_list': res_list, 'partition_exist': False}
    else:
        partition_version = partition_info_dict.get(model_system_key)
        return {'partition_version': partition_version, 'query_list': res_list, 'partition_exist': True}
