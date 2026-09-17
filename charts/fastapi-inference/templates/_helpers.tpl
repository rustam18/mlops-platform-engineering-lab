{{- define "fastapi-inference.name" -}}
fastapi-inference
{{- end -}}

{{- define "fastapi-inference.labels" -}}
app: {{ include "fastapi-inference.name" . }}
app.kubernetes.io/name: {{ include "fastapi-inference.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}
