import { FC, useEffect, useState } from "react";
import { Data } from "./models/Data";

const DataTable: FC = () => {
  const [data, setData] = useState<Data[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/data?n=10")
      .then((response) => response.json())
      .then((response) => setData(response));
  }, []);

  return (
    <div className="data-table">
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Lastname</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d, idx) => (
            <tr>
              <td>{d.name}</td>
              <td>{d.lastname}</td>
              <td>{d.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
