#!/bin/bash

## delete pvc
oc get pvc --no-headers -o custom-columns=NAME:.metadata.name \
        | grep '^shared-pvc-titanic' \
        | xargs -r oc delete pvc

oc apply -f openshift/tasks/preprocess-task.yaml
oc apply -f openshift/tasks/train-task.yaml
oc apply -f openshift/tasks/build-task.yaml     
oc apply -f openshift/tasks/deploy-task.yaml 

oc apply -f openshift/tasks/pipeline.yaml
oc apply -f openshift/taskruns/pipelinerun.yaml

