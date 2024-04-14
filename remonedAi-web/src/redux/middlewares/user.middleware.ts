import { Middleware } from "redux";
import {
	apiRequest,
	postLoginUserProcess,
	postRegisterUserProcess,
	postLoginUserError,
	postLoginUserSuccess,
	postRegisterUserError,
	postRegisterUserSuccess,
} from "../actions";
import {
	POST_REGISTER_USER_ERROR,
	POST_REGISTER_USER_SUCCESS,
	POST_LOGIN_USER_ERROR,
	POST_LOGIN_USER_SUCCESS,
} from "../constants";

import { storage } from "@/src/helpers";

const USER_URL = "http://localhost:3001/user";

const userProcess: Middleware =
	({ dispatch }) =>
	(next) =>
	(action) => {
		next(action);
		if (postRegisterUserProcess.match(action)) {
			dispatch(
				apiRequest(
					"POST",
					`${USER_URL}/register`,
					action.payload,
					POST_REGISTER_USER_SUCCESS,
					POST_REGISTER_USER_ERROR
				)
			);
		}
		if (postLoginUserProcess.match(action)) {
			dispatch(
				apiRequest(
					"POST",
					`${USER_URL}/login`,
					action.payload,
					POST_LOGIN_USER_SUCCESS,
					POST_LOGIN_USER_ERROR
				)
			);
		}
	};

const userSuccess: Middleware =
	({ dispatch }) =>
	(next) =>
	(action) => {
		next(action);
		if (postRegisterUserSuccess.match(action)) {
			console.log(action.payload.data);
			storage.set("user", action.payload.data);
		}
		if (postLoginUserSuccess.match(action)) {
			console.log(action.payload.data);
			storage.set("user", action.payload.data);
		}
	};

const userErrors: Middleware =
	({ dispatch }) =>
	(next) =>
	(action) => {
		next(action);
		if (postRegisterUserError.match(action)) {
			console.log(action.payload);
		}
		if (postLoginUserError.match(action)) {
			console.log(action.payload);
		}
	};

export const userMiddleware = [userProcess, userSuccess, userErrors];