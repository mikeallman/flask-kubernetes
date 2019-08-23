start_db:
	docker run --rm --name postgres -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $$HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres:12-alpine

stop_db:
	docker kill postgres

build_image:
	cd flask-app; docker build --tag eu.gcr.io/mike-237810/customer_service:1.1.0 .

push_image:
	docker push eu.gcr.io/mike-237810/customer_service:1.1.0

rbac:
	helm init --upgrade --history-max 50
	kubectl create serviceaccount --namespace kube-system tiller
	kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
	kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'

flux:
	kubectl apply -f https://raw.githubusercontent.com/fluxcd/flux/helm-0.10.1/deploy-helm/flux-helm-release-crd.yaml
	helm install --name flux --set git.url=git@github.com:mikeallman/flask-kubernetes --set helmOperator.create=true --set helmOperator.createCRD=false --namespace flux fluxcd/flux

deploy_app:
	helm install ./helm
