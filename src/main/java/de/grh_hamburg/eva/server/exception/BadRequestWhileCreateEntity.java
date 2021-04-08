package de.grh_hamburg.eva.server.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(code = HttpStatus.BAD_REQUEST, reason = "Could not parse ID from request. Maybe the ID is not an int?")
public class BadRequestWhileCreateEntity extends RuntimeException {
}
