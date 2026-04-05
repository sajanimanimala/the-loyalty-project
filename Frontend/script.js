document.getElementById("form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const feedback = document.getElementById("feedback").value;

    let formData = new FormData();
    formData.append("feedback", feedback);

    try {
        let res = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });

        let data = await res.json();

        let output = "";

        // ✅ FIXED: access correct structure
        const issues = data.analysis.issues;

        if (!issues || issues.length === 0) {
            output = `<p class="text-red-400 font-semibold text-lg">No issues detected</p>`;
        } else {
            issues.forEach(item => {
                output += `
                <div class="result-card bg-white/10 backdrop-blur-md border border-white/15 p-5 rounded-2xl shadow-xl mb-4">
                    <h3 class="text-2xl font-bold text-cyan-300 capitalize mb-4">
                        ${item.issue.replace("_", " ")}
                    </h3>

                    <p class="mt-2 text-gray-100 text-base leading-relaxed">
                        <span class="font-semibold text-white">Solutions:</span> 
                        ${item.solutions.join(", ")}
                    </p>

                    <p class="mt-3 text-gray-100 text-base leading-relaxed">
                        <span class="font-semibold text-white">Template:</span> 
                        ${item.template.title}
                    </p>

                    <ul class="list-disc ml-5 mt-4 space-y-2 text-sm md:text-base text-gray-200 leading-relaxed">
                        ${item.template.steps.map(step => `<li>${step}</li>`).join("")}
                    </ul>
                </div>
                `;
            });
        }

        document.getElementById("result").innerHTML = output;

    } catch (error) {
        document.getElementById("result").innerHTML =
            `<p class="text-red-400 font-semibold text-lg">Error connecting to backend</p>`;
        console.error(error);
    }
});


// 🔹 CLEAR BUTTON
document.getElementById("clearBtn").addEventListener("click", () => {
    document.getElementById("feedback").value = "";
    document.getElementById("result").innerHTML = "";
});