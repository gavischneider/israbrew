import React, { useState, useEffect } from "react";
import "./App.scss";
import { TabsBar } from "./components/TabsBar";

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch("/time")
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
      });
  }, []);

  return (
    <div className="App">
      <TabsBar />

      <p>The current time is {currentTime}</p>
    </div>
  );
}

export default App;
