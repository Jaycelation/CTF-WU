const fastify = require("fastify")({ logger: true });
const fs = require("fs");
const path = require("path");
const invalidEqCharacters = /[^0-9\s+\-^/*]/;

/* https://www.npmjs.com/package/dompurify example: */
const createDOMPurify = require("dompurify");
const { JSDOM } = require("jsdom");
const { report } = require("./bot");
const window = new JSDOM("").window;
const DOMPurify = createDOMPurify(window);
const clean = (s) => DOMPurify.sanitize(s, {});
/* https://www.npmjs.com/package/dompurify end example */

fastify.register(require("@fastify/static"), {
	root: path.join(__dirname, "build"),
	prefix: "/",
});

fastify.get("/", async (req, reply) => {
	reply.type("text/html").send(fs.readFileSync("index.html", "utf-8"));
});

fastify.get("/err", async (req, reply) => {
	if (typeof req.query.s !== "string") {
		return reply.status(500).send("hacker");
	}
	if (req.query.s.length > 512) {
		return reply.status(500).send("hacker");
	}
	reply.type("text/html").send(`
<html>
	<head>
		<style>
			* {
				color: red;
			}
		</style>
	</head>
	<body>
		${DOMPurify.sanitize(req.query.s)}
	</body>
</html>
`);
});

fastify.get("/test", async (req, reply) => {
	reply.type("text/html").send(req.query?.html ?? "req query html empty");
});

fastify.post("/solve", async (req, reply) => {
	const { eq } = req.body;

	if (typeof eq !== "string") {
		return reply.send({
			success: false,
			message: "not this time you <b>hacker!!</b>",
		});
	}
	if (eq.length < 0 || eq.length > 50) {
		return reply.send({
			success: false,
			message:
				"sorry but your <i>equation</i> <u>must</u> be at most 50 characters long.",
		});
	}
	if (invalidEqCharacters.test(eq)) {
		return reply.send({
			success: false,
			message:
				"you can't use anything else than <code>numbers</code>, <i>whitespaces</i>, <code>&plus;</code>, <code>-</code>, <code>&Hat;</code>, <code>&sol;</code> and <code>&ast;</code>. Unfortunately due to some <b>hackers</b>, we <u>had to</u> limit our great calculator..",
		});
	}
	try {
		return reply.send({
			success: true,
			data: {
				result: String(eval(eq)),
			},
		});
	} catch (err) {
		console.log("solve failed", { err, eq });
		return reply.send({
			success: false,
			message: "something went wrong.",
		});
	}
});

fastify.get("/report", async (req, reply) => {
	reply.type("text/html").send(fs.readFileSync("report.html", "utf-8"));
});

fastify.post("/report", async (req, reply) => {
	try {
		const m = await report(req.body.data);
		return reply.send({
			success: true,
			message: m,
		});
	} catch (err) {
		return reply.send({
			success: false,
			message: err?.message ?? "something went wrong",
		});
	}
});

fastify.listen({ port: 3000, host: "0.0.0.0" }, (err, address) => {
	if (err) {
		console.error(err);
		process.exit(1);
	}
	console.log(`Server running at ${address}`);
});
