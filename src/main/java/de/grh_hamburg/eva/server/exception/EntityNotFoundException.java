package de.grh_hamburg.eva.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.NOT_FOUND, reason = "Entity not found.")
public class EntityNotFoundException extends RuntimeException {
}
