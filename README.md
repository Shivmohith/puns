# Punny App

## OC Commands

- oc project shivmohith
- oc get all
- oc new-app --template <name of template> # create an app using the template
- oc create -f <local template file name> # creates template
- oc status
- oc delete template <name of template>
- oc delete --all all
- oc import-image approved-apache:2.4 --from=bitnami/apache:2.4 --confirm