# Demo to play around with RabbitMQ federation
To start:
```bash
docker compose up
```

Follow the steps here to setup the federation: https://www.rabbitmq.com/docs/federation#tutorial
The steps should be performed on the downstream server. Credentials can be applied in the URI.
The downstream server will use the credentials to connect to the upstream server as a user.

In our situation, we will want the main GPX cloud broker to be the downstream server which
connects to multiple, selfhosted upstream servers.