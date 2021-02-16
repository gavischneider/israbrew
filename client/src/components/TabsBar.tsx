import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
import "../tabs.scss";
import { BeersJSON } from "../types/BeersJSON";
import { BeerGrid } from "./BeerGrid";

export const TabsBar = () => {
  const initialState = {
    beerandbeyond: [],
    biratenu: [],
    mendelsonheshin: [],
    beerz: [],
    beerbazaar: [],
    keshetteamim: [],
    tivtaam: [],
  };

  const [beers, setBeers] = useState<BeersJSON>(initialState);

  useEffect(() => {
    fetch("/api/beers")
      .then((res) => res.json())
      .then((data) => {
        setBeers(data.beers);
      });
  }, []);

  return (
    <div>
      <Tabs className="bg-gray-900">
        <img src="logo5.png" alt="israbrew logo" className=" ml-4 pt-4" />

        <TabList className="text-white">
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Home
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Beer And Beyond
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Biratenu
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Mendelson Heshin
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            BeerZ
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Beer Bazaar
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Keshet Teamim
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity))",
            }}
          >
            Tiv Taam
          </Tab>
        </TabList>

        <TabPanel>
          <div className="bg-gray-900">
            <div className="w-100 h-screen mx-auto p-10">
              <div className="h-5/6 pt-16">
                <h1 className="text-white text-3xl">Welcome to IsraBrew!</h1>
                <br />
                <br />
                <br />
                <div className=" bg-white mx-auto rounded-full w-max">
                  <img
                    src="logo1.png"
                    alt="israbrew logo"
                    className="mx-auto"
                  />
                </div>
                <br />
                <br />
                <br />
                <h2 className="text-white text-xl">
                  See what beers are currently available from our favorite
                  suppliers!
                </h2>
              </div>
              <br />

              <h1 className="text-white object-bottom sticky">
                Made with 🍺 by{" "}
                <a
                  className="text-yellow-200"
                  target="_blank"
                  rel="noopener noreferrer"
                  href="https://gavischneider.github.io/Personal-Site/"
                >
                  Gavi Schneider
                </a>
              </h1>
            </div>
          </div>
        </TabPanel>

        <TabPanel>
          <BeerGrid beers={beers.beerandbeyond} supplier={"Beer And Beyond"} />
        </TabPanel>
        <TabPanel>
          <BeerGrid beers={beers.biratenu} supplier={"Biratenu"} />
        </TabPanel>
        <TabPanel>
          <BeerGrid
            beers={beers.mendelsonheshin}
            supplier={"Mendelson Heshin"}
          />
        </TabPanel>
        <TabPanel>
          <BeerGrid beers={beers.beerz} supplier={"BeerZ"} />
        </TabPanel>
        <TabPanel>
          <BeerGrid beers={beers.beerbazaar} supplier={"Beer Bazaar"} />
        </TabPanel>
        <TabPanel>
          <BeerGrid beers={beers.keshetteamim} supplier={"Keshet Teamim"} />
        </TabPanel>
        <TabPanel>
          <BeerGrid beers={beers.tivtaam} supplier={"Tiv Taam"} />
        </TabPanel>
      </Tabs>
    </div>
  );
};
