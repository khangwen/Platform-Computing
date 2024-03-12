import './App.css';

function App() {
  let cntr = 0;
  const newPageUrl = "https://github.com/khangwen";

  const clickEvent = () => {
    cntr++;
    // let text = "Clicked " + cntr + " times!";
    window.open(newPageUrl, "_blank")
    // console.log("You clicked the button " + cntr + " times!");
    // document.getElementsByClassName("button")[0].style.backgroundColor = "red";
    // document.getElementsByClassName("button")[0].textContent = "Clicked!";
    // alert("You clicked the button!");
  }

  return (
    <div class="maincontainer">
      <header>
        <h1>about.</h1>
      </header>

      <div class="intro">
        <p>I'm a California based Computer Science major, currently studying at CSUSB. I expect to graduate in May
          2024.
        </p>
      </div>

      <div class="education">
        <h2>education.</h2>
        <p>Currently, I've taken many courses including: Data Structures and Algorithms, Algorithm Analysis, Web
          Application Development, Software
          Engineering, Database Systems, Differential Equations and Linear Algebra, Calculus III, Artificial
          Intelligence, Operating Systems, Parallel Algorithms, Computer Architecture.</p>
      </div>

      <div id="skills">
        <h2>skills.</h2>
        <p>My skills include: JavaScript, Python, TypeScript, C++, C, Java, SQL. I've worked with tools and
          technologies
          such as Node.js, React.js, Express.js, Next.js, Git / GitHub, VSCode, Azure SQL Database</p>
      </div>

      <div class="contact">
        <h2>contact.</h2>
        <p>You can contact me at: khangwen197@gmail.com ● linkedin.com/in/alannguyen197</p>
      </div>

      <div class="github">
        <h2>github.</h2>
        <button type="button" className="button" onClick={clickEvent}>Click Here For My Github!</button>
      </div>

      <img src="/scenery.jpg" alt="scenery" class="scenery" />



    </div>
  );
}

export default App;
