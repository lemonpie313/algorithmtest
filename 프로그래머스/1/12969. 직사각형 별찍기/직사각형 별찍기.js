process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
	const n = data.split(" ");
	const a = Number(n[0]);
	const b = Number(n[1]);

	for (let n = 0; n < b; n++) {
		console.log("*".repeat(a));
	}
});