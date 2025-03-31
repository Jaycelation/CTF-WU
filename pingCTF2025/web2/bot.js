import puppeteer from "puppeteer";

const FLAG = process.env.FLAG ?? "ping{FAKE}";

const isSafeSuffix = (s) => {
	return !s.includes(".");
};

export const report = async (data) => {
	if (typeof data !== "string") {
		throw new Error("invalid data");
	}
	if (!isSafeSuffix(data)) {
		throw new Error("invalid data");
	}

	const browser = await puppeteer.launch({
		headless: "new",
		args: [
			"--disable-gpu",
			"--no-sandbox",
			"--js-flags=--noexpose_wasm,--jitless",
		],
		executablePath: "/usr/bin/chromium-browser",
	});
	const page = await browser.newPage();
	await page.setCookie({
		name: "FLAG",
		value: FLAG,
		domain: "localhost",
		path: "/",
	});
	await page.goto(`http://localhost:3000/${data}`);
	await new Promise((resolve) => setTimeout(resolve, 1000));
	await browser.close();
};
