import { FC, useEffect, useState } from "react";
import { TodoItem } from "./models/Data";

const DataTable: FC = () => {
  const [data, setData] = useState<TodoItem[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/data?n=10")
      .then((response) => response.json())
      .then((json) => setData(json));
  }, []);

  return (
    <div className="data-table">
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Age</th>
            <th>Content</th>
            <th>Priority</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d, idx) => (
            <tr key={idx}>
              <td>{d.id}</td>
              <td>{d.age}</td>
              <td>{d.content}</td>
              <td>{d.priority}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
