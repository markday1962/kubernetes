from kubernetes import client, config


def main():
    # Configs can be set in Configuration class directly or using helper utility
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    ret = v1.list_namespaced_pod("cipher3")
    print(ret)

    apis_api = client.AppsV1Api()
    resp = apis_api.list_namespaced_deployment(namespace="cipher3")
    for i in resp.items:
        print(i.metadata.labels)
        print()


if __name__ == "__main__":
    main()
