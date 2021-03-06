## Parameters

The following tables lists the configurable parameters of the PostgreSQL chart and their `default` values.

Parameter | Description | Default
--------- | ----------- | -------
`global.postgresql.postgresqlDatabase` | PostgreSQL database | `rems`
`global.postgresql.postgresqlUsername` | PostgreSQL username | `random_un`
`global.postgresql.postgresqlPassword` | PostgreSQL admin password | `random_pw`
`image.registry` | PostgreSQL Image registry | `docker.io`
`image.repository` | PostgreSQL Image name | `bitnami/postgresql`
`image.tag` | PostgreSQL Image tag | `11.9.0-debian-10-r48`
`image.pullPolicy` | PostgreSQL Image pull policy | `IfNotPresent`
`image.debug` | Specify if debug values should be set |	`false`
`volumePermissions.enabled` | Enable init container that changes volume permissions in the data directory (for cases where the default k8s runAsUser and fsUser values do not work) | `false`
`volumePermissions.image.registry` | Init container volume-permissions image registry |	`docker.io`
`volumePermissions.image.repository` | Init container volume-permissions image name | `bitnami/minideb`
`volumePermissions.image.tag` |	Init container volume-permissions image tag | `buster`
`volumePermissions.image.pullPolicy` | Init container volume-permissions image pull policy | `Always`
`volumePermissions.securityContext.runAsUser` |	User ID for the init container (when facing issues in OpenShift or uid unknown, try value "auto") |	`0`
`securityContext.enabled` |	Enable security context | `true`
`securityContext.fsGroup` |	Group ID for the pod | `1001`
`containerSecurityContext.enabled` | Enable security context for the container | `true`
`containerSecurityContext.runAsUser` | User for the securityContext | `1001`
`serviceAccount.enabled` | Enable service account (Note: Service Account will only be automatically created if serviceAccount.name is not set) | `true`
`psp.create` | Create Pod Security Policy |	`true`
`rbac.create` |	Create Role and RoleBinding (required for PSP to work) | `true`
`replication.enabled` |	Enable replication | `false`
`replication.user` | Replication user |	`repl_user`
`replication.password` | Replication user password | `repl_password`
`replication.slaveReplicas` | Number of slaves replicas | `1`
`replication.synchronousCommit` | Set synchronous commit mode. Allowed values: on, remote_apply, remote_write, local and off | `off`
`replication.numSynchronousReplicas` | Number of replicas that will have synchronous replication. Note: Cannot be greater than replication.readReplicas | `0`
`replication.applicationName` |	Cluster application name. Useful for advanced replication settings | `my_application`
`postgresqlUsername` | PostgreSQL user (creates a non-admin user when postgresqlUsername is not postgres) |	`postgres`
`postgresqlDataDir` | PostgreSQL data dir folder | `/bitnami/postgresql/data`
`extraEnv` | Any extra environment variables you would like to pass on to the pod. The value is evaluated as a template. | `[]`
`masterAsStandBy.enabled` | Whether to enable current cluster's Master as standby server of another cluster or not. | `false`
`audit.logHostname` | Add client hostnames to the log file | `false`
`audit.logConnections` | Add client log-in operations to the log file | `false`
`audit.logDisconnections` |	Add client log-outs operations to the log file | `false`
`audit.pgAuditLog` | Add operations to log using the pgAudit extension | `''`
`audit.pgAuditLogCatalog` | Log catalog using pgAudit | `off`
`audit.clientMinMessages` |	Message log level to share with the user | `error`
`audit.logLinePrefix` |	Template string for the log line prefix | `''`
`audit.logTimezone` | Timezone for the log timestamps | `''`
`postgresqlSharedPreloadLibraries` | Shared preload libraries (comma-separated list) | `pgaudit`
`postgresqlMaxConnections` | Maximum total connections | `nil`
`postgresqlPostgresConnectionLimit` | Maximum total connections for the postgres user |	`nil`
`postgresqlDbUserConnectionLimit` | Maximum total connections for the non-admin user | `nil`
`postgresqlTcpKeepalivesInterval` |	TCP keepalives interval | `nil`
`postgresqlTcpKeepalivesIdle` |	TCP keepalives idle | `nil`
`postgresqlTcpKeepalivesCount` | TCP keepalives count |	`nil`
`postgresqlStatementTimeout` | Statement timeout | `nil`
`postgresqlPghbaRemoveFilters` | Comma-separated list of patterns to remove from the pg_hba.conf file |	`nil`
`ldap.enabled` | Enable LDAP support | `false`
`ldap.url` | LDAP URL beginning in the form `ldap[s]://host[:port]/basedn[?[attribute][?[scope][?[filter]]]]` | `''`
`ldap.server` |	IP address or name of the LDAP server |	`''`
`ldap.port` | Port number on the LDAP server to connect to | `''`
`ldap.prefix` |	String to prepend to the user name when forming the DN to bind | `''`
`ldap.suffix` |	String to append to the user name when forming the DN to bind | `''`
`ldap.baseDN` |	Root DN to begin the search for the user in | `''`
`ldap.bindDN` |	DN of user to bind to LDAP | `''`
`ldap.bind_password` | Password for the user to bind to LDAP| `nil`
`ldap.search_attr` | Attribute to match agains the user name in the search | `''`
`ldap.search_filter` | The search filter to use when doing search+bind `authentication` | `''`
`ldap.scheme` |	Set to ldaps to use LDAPS | `''`
`ldap.tls` | Set to 1 to use TLS encryption | `false`
`service.type`  | Kubernetes Service type |	`ClusterIP`
`service.port` | PostgreSQL port | `5432`
`service.annotations` |	Annotations for PostgreSQL service | `{}`
`shmVolume.enabled` | Enable emptyDir volume for /dev/shm for primary and read replica(s) Pod(s) | `true`
`shmVolume.chmod.enabled` |	Run at init chmod 777 of the /dev/shm (ignored if `volumePermissions.enabled` is false) | `true`
`persistence.enabled` |	Enable persistence using PVC | `true`
`persistence.mountPath` | Path to mount the volume at | `/bitnami/postgresql`
`persistence.subPath` |	Subdirectory of the volume to mount at | `''`
`persistence.accessModes` |	PVC Access Mode for PostgreSQL volume | `ReadWriteOnce`
`persistence.size` | PVC Storage Request for PostgreSQL volume | `8Gi`
`persistence.annotations` |	Annotations for the PVC | `{}`
`updateStrategy.type` |	Update strategy policy type | `RollingUpdate`
`master.nodeSelector` | Node labels for pod assignment (postgresql master) | `{}`
`master.affinity` | Affinity labels for pod assignment (postgresql master)| `{}`
`master.tolerations` | Toleration labels for pod assignment (postgresql master) | `[]`
`master.labels` | Map of labels to add to the statefulset (postgresql master) | `{}`
`master.annotations` | Map of annotations to add to the statefulset (postgresql master) | `{}`
`master.podLabels` | Map of labels to add to the pods (postgresql master) | `{}`
`master.podAnnotations` | Map of annotations to add to the pods (postgresql master) | `{}`
`master.priorityClassName` | Priority Class to use for each pod (postgresql master) | `''`
`master.extraInitContainers` | Additional init containers to add to the pods (postgresql master) | `[]`
`master.extraVolumeMounts` | Additional volume mounts to add to the pods (postgresql master) | `[]`
`master.extraVolumes` | Additional volumes to add to the pods (postgresql master) | `[]`
`master.sidecars` | Add additional containers to the pod | `[]`
`master.service` | Allows using different services (type, nodePort, clusterIP) | `{}`
`slave.nodeSelector` | Node labels for pod assignment (postgresql slave) | `{}`
`slave.affinity` | Affinity labels for pod assignment (postgresql slave)| `{}`
`slave.tolerations` | Toleration labels for pod assignment (postgresql slave) | `[]`
`slave.labels` | Map of labels to add to the statefulset (postgresql slave) | `{}`
`slave.annotations` | Map of annotations to add to the statefulset (postgresql slave) | `{}`
`slave.podLabels` | Map of labels to add to the pods (postgresql slave) | `{}`
`slave.podAnnotations` | Map of annotations to add to the pods (postgresql slave) | `{}`
`slave.priorityClassName` | Priority Class to use for each pod (postgresql slave) | `''`
`slave.extraInitContainers` | Additional init containers to add to the pods (postgresql slave) | `[]`
`slave.extraVolumeMounts` | Additional volume mounts to add to the pods (postgresql slave) | `[]`
`slave.extraVolumes` | Additional volumes to add to the pods (postgresql slave) | `[]`
`slave.sidecars` | Add additional containers to the pod | `[]`
`slave.service` | Allows using different services (type, nodePort, clusterIP) | `{}`
`slave.persistence.enabled` | Use a PVC to persist data (slave node) | `true`
`slave.resources` | Slave CPU/Memory resource requests/limits | `{}`
`resources.requests.memory` | Memory resource request | `256Mi`
`resources.requests.cpu` | CPU resource request | `250m`
`commonAnnotations` | Annotations to be added to all deployed resources (rendered as a template) | `{}`
`networkPolicy.enabled` | Enable NetworkPolicy | `false`
`networkPolicy.allowExternal` |	Don't require client label for connections | `true`
`networkPolicy.explicitNamespacesSelector` | A Kubernetes LabelSelector to explicitly select namespaces from which ingress traffic could be allowed | `{}`
`livenessProbe.enabled` | Would you like a livenessProbe to be enabled | `true`
`livenessProbe.initialDelaySeconds` | Delay before liveness probe is initiated | `30`
`livenessProbe.periodSeconds` |	How often to perform the probe | `10`
`livenessProbe.timeoutSeconds` | When the probe times out | `5`
`livenessProbe.failureThreshold` | Minimum consecutive failures for the probe to be considered failed after having succeeded | `6`
`livenessProbe.successThreshold` | Minimum consecutive successes for the probe to be considered successful after having failed | `1`
`readinessProbe.enabled` | would you like a readinessProbe to be enabled | `false`
`readinessProbe.initialDelaySeconds` | Delay before readiness probe is initiated | `6`
`readinessProbe.periodSeconds` | How often to perform the probe | `10`
`readinessProbe.timeoutSeconds` | When the probe times out | `5`
`readinessProbe.failureThreshold` | Minimum consecutive failures for the probe to be considered failed after having succeeded | `6`
`readinessProbe.successThreshold` |	Minimum consecutive successes for the probe to be considered successful after having failed | `1`
`customLivenessProbe` | Override default liveness probe | `{}`
`customReadinessProbe` | Override default readiness probe | `{}`
`tls.enabled` |	Enable TLS traffic support | `false`
`tls.preferServerCiphers`| Whether to use the server's TLS cipher preferences rather than the client's | `true`
`tls.certificatesSecret` | Name of an existing secret that contains the certificates | `''`
`tls.certFilename` | Certificate filename |	`''`
`tls.certKeyFilename` |	Certificate key filename | `''`
`tls.certCAFilename` | CA Certificate filename. If provided, PostgreSQL will authenticate TLS/SSL clients by requesting them a certificate | `nil`
`tls.crlFilename` |	File containing a Certificate Revocation List |	`nil`
`metrics.enabled` |	Start a prometheus exporter | `false`
`metrics.service.type` | Kubernetes Service type | `ClusterIP`
`metrics.service.annotations.prometheus.io/scrape` | Additional annotation for metrics exporter pod | `'true'`
`metrics.service.annotations.prometheus.io/port` | Additional annotation for metrics exporter pod | `'9187'`
`metrics.service.loadBalancerIP` | loadBalancerIP if redis metrics service type is LoadBalancer  | `nil`
`metrics.serviceMonitor.enabled` | Set this to true to create ServiceMonitor for Prometheus operator | `false`
`metrics.serviceMonitor.additionalLabels` |	Additional labels that can be used so ServiceMonitor will be discovered by Prometheus | `{}`
`metrics.prometheusRule.enabled` | Set this to true to create prometheusRules for Prometheus operator | `false`
`metrics.prometheusRule.additionalLabels` |	Additional labels that can be used so prometheusRules will be discovered by Prometheus | `{}`
`metrics.prometheusRule.namespace` | namespace where prometheusRules resource should be created	the same namespace as postgresql | `''`
`metrics.prometheusRule.rules` | `rules` to be created, check values for an example | `[]`
`metrics.image.registry` | PostgreSQL Exporter Image registry | `docker.io`
`metrics.image.repository` | PostgreSQL Exporter Image name | `bitnami/postgres-exporter`
`metrics.image.tag` | PostgreSQL Exporter Image tag | `0.8.0-debian-10-r242`
`metrics.image.pullPolicy` | PostgreSQL Exporter Image pull policy | `IfNotPresent`
`metrics.extraEnvVars` | Extra environment variables to add to exporter | `{}`
`metrics.securityContext.enabled` | Enable security context for metrics | `false`
`metrics.securityContext.runAsUser` | User ID for the container for metrics | `1001`
`metrics.livenessProbe.enabled` | Enable/disable the Liveness Check of Prometheus metrics exporter | `true`
`metrics.livenessProbe.initialDelaySeconds` | Delay before liveness probe is initiated | `5`
`metrics.livenessProbe.periodSeconds` | How often to perform the probe | `10`
`metrics.livenessProbe.timeoutSeconds` | When the probe times out |	`5`
`metrics.livenessProbe.failureThreshold` | Minimum consecutive failures for the probe to be considered failed after having succeeded | `6`
`metrics.livenessProbe.successThreshold` | Minimum consecutive successes for the probe to be considered successful after having failed | `1`
`metrics.readinessProbe.enabled` | would you like a readinessProbe to be enabled | `true`
`metrics.readinessProbe.initialDelaySeconds` | Delay before liveness probe is initiated | `5`
`metrics.readinessProbe.periodSeconds` | How often to perform the probe | `10`
`metrics.readinessProbe.timeoutSeconds` | When the probe times out | `5`
`metrics.readinessProbe.failureThreshold` |	Minimum consecutive failures for the probe to be considered failed after having succeeded | `6`
`metrics.readinessProbe.successThreshold` | Minimum consecutive successes for the probe to be considered successful after having failed | `1`
`extraDeploy` | Array of extra objects to deploy with the release (evaluated as a template) | `[]`
