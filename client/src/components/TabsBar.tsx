import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";
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
        console.log("DATA!!!!!!!!!!!!");
        console.log(data.beers.beerbazaar);
        setBeers(data.beers);
      });
  }, []);

  return (
    <div>
      <Tabs className="bg-gray-900">
        <h1 className="text-left text-white pt-2 pl-2">IsraBrew</h1>
        <TabList className="text-white">
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Home
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Beer And Beyond
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Biratenu
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Mendelson Heshin
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            BeerZ
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Beer Bazaar
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Keshet Teamim
          </Tab>
          <Tab
            style={{
              backgroundColor:
                "background-color: rgba(17, 24, 39, var(--tw-bg-opacity));",
            }}
          >
            Tiv Taam
          </Tab>
        </TabList>

        <TabPanel>
          <div className="bg-gray-900 min-h-screen">
            <div className="h-80 w-80 mx-auto p-10">
              <h1 className="text-white text-xl">Welcome to IsraBrew!</h1>
            </div>
            <h1 className="text-white object-bottom sticky">
              Made with 🍺 by Gavi Schneider
            </h1>
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
