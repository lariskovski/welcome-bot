IMAGE_NAME=welcome-bot

ifndef API_TOKEN
$(error API_TOKEN is not set. Please set it before trying again.)
endif

all: run
	@echo "All good."

build:
	@docker build -t ${IMAGE_NAME} .

test:
	@yes | docker scan ${IMAGE_NAME}

run: build
	@docker run -d --name ${IMAGE_NAME} --env API_TOKEN=${API_TOKEN} ${IMAGE_NAME}

clean:
	@docker rm -f ${IMAGE_NAME}
	@docker rmi ${IMAGE_NAME}