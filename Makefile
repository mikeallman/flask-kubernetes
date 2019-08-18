start_db:
	docker run --rm --name postgres -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $$HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres:12-alpine

stop_db:
	docker kill postgres

build_image:
	docker build --tag eu.gcr.io/mike-237810/customer_service:1.0.0 .

push_image:
	docker push eu.gcr.io/mike-237810/customer_service:1.0.0

rbac:
	kubectl create serviceaccount --namespace kube-system tiller
	kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
	kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}

deploy_app:
	helm install ./helm
