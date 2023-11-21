
<script>
    var myName = prompt("Please enter your name");
    alert("Welcome " + myName);
    var val = prompt("Enter the current temperature");
    if (val > 30) {
        alert("Too hot!");
    }
    else if (val < 20) {
        alert("Too cold!");
    }
    else {
        alert("Temp. is fine.")
    }
</script>

JS asks temp and if condition responses.JS



    < body >
    <h1> The heading </h1>
    <p id="special">A paragraph</p>
    <p>A second paragraph</p>
    <p id="para3">A third paragraph is changed in the JS</p>
    <ul>
        <li id="item1">item 1</li>
        <li>item 2</li>
        <li>item 3</li>
    </ul>
    <script>
        var heading1 = document.querySelector("h1");
        heading1.style.color = "red";

        var para2 = document.querySelector("#special");
        para2.style.fontWeight = "bold";
        para2.textContent = "Content changed through JS!"
        para2.style.color = "#07c700";

        var list = document.querySelector("ul");
        list.innerHTML = "<li>item1JS</li> <li>item2JS</li><li>item3JS</li> ";

        var para3 = document.querySelector("#para3");
        para3.style.backgroundColor = "aqua";
        para3.style.fontStyle = "italic";
    </script>
</body >



< !DOCTYPE html >
    <html>

        <head>
            <title> </title>
        </head>


        <body>
            <h1> The heading </h1>
            <p id="special">A paragraph</p>
            <p>A second paragraph</p>
            <p id="para3">A third paragraph is changed in the...</p>
            <ul>
                <li id="item1">item 1</li>
                <li>item 2</li>
                <li>item 3</li>
            </ul>
            <script>
                var heading1 = document.querySelector("h1");
                heading1.style.color = "red";

                var para2 = document.querySelector("#special");
                para2.style.fontWeight = "bold";
                para2.textContent = "Content changed through JS!"
                para2.style.color = "#07c700";

                var list = document.querySelector("ul");
                list.innerHTML = "<li>item1JS</li> <li>item2JS</li><li>item3JS</li> ";

                var para3 = document.querySelector("#para3");
                para3.style.backgroundColor = "aqua";
                para3.style.fontStyle = "italic";
            </script>
        </body>

    </html>