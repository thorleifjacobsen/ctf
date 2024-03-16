# Ticket API

This API allows to upload, and then verify ticket for events (in example CTF challenge 🚩)

## Endpoints

### Upload

Upload allows you to upload new tickets to the system. These tickets can be then verified on the event entrance:

> curl -X POST -F "file=@/path/to/ticket/file.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/upload

### Verify

While integrating your entrance gate thingy call this endpoint to verify if the ticket being shown to you is not forged:

> curl -X POST -F "file=@/path/to/ticket/file.pdf" https://ticket-api-061f5e195e3d.1753ctf.com/verify

## Security

Yes.