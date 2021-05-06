from kubernetes import client, config
from kubernetes.client.rest import ApiException


def scale_deployment(ns, current_selector, new_selector):
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    ret = v1.list_namespaced_service(ns)
    try:
        for s in ret.items:
            if s.spec.selector is not None:
                for k, v in s.spec.selector.items():
                    if k == "backend" and v == current_selector:
                        name = s.metadata.name
                        body = {"spec": {"selector": {"backend": new_selector}}}
                        ps = v1.patch_namespaced_service(name, ns, body)
                        print(ps)
    except ApiException as e:
        print("ApiException {}\n".format(e))


if __name__ == "__main__":
    scale_deployment("cipher3", "zaphod", "zaphod")