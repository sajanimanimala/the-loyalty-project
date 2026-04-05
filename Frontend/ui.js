document.getElementById("form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const imageFile = document.getElementById("image").files[0];

    let formData = new FormData();
    formData.append("image", imageFile);

    try {
        let res = await fetch("http://127.0.0.1:8000/analyze-ui", {
            method: "POST",
            body: formData
        });

        let data = await res.json();

        let output = `
        <div class="result-card bg-white/10 backdrop-blur-md border border-white/15 p-5 rounded-2xl shadow-xl">
            <h3 class="text-2xl font-bold text-emerald-300 mb-4">Visual Insights</h3>
            <ul class="list-disc ml-5 mt-2 space-y-2 text-gray-100 text-base leading-relaxed">
                ${data.image_insights.map(i => `<li>${i}</li>`).join("")}
            </ul>
        </div>
        `;

        document.getElementById("result").innerHTML = output;

    } catch (error) {
        document.getElementById("result").innerHTML =
            `<p class="text-red-400 font-semibold text-lg">Error analyzing UI. Please try again.</p>`;
    }
});

document.getElementById("clearBtn").addEventListener("click", () => {
    document.getElementById("image").value = "";
    document.getElementById("result").innerHTML = "";
});