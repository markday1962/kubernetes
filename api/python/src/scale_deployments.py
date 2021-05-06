from kubernetes import client, config
from kubernetes.client.rest import ApiException


def scale_deployment(ns, backend, replicas):
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    apis_api = client.AppsV1Api()
    resp = apis_api.list_namespaced_deployment(namespace=ns)
    for i in resp.items:
        for k, v in i.metadata.labels.items():
            if k == "backend" and v == backend:
                name = i.metadata.name
                namespace = "cipher3"
                body = {"spec": {"replicas": replicas}}
                try:
                    print("Scaling {} to {} pods".format(name, replicas))
                    ret = apis_api.patch_namespaced_deployment_scale(name, namespace, body)
                    #print(ret)
                except ApiException as e:
                    print("Exception when calling AppsV1Api->patch_namespaced_deployment_scale: {}}\n".format(e))


if __name__ == "__main__":
    scale_deployment("cipher3", "marvin", 0)
