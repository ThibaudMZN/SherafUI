import { FC, ReactNode, useEffect, useState, useMemo, useCallback } from "react";
import {SherafObject, TodoItem} from "./models/Data";


const DataTable: FC = () => {
  const [data, setData] = useState<SherafObject[]>([]);

  const getDatatypeKeys = useCallback((datatype: any) => Object.keys(datatype), [])

  const getLine = useCallback((datatype: any) => getDatatypeKeys(datatype)
      .map((key) => <td>{datatype[key]}</td>), [getDatatypeKeys])


  useEffect(() => {
    fetch(`${process.env.REACT_APP_ROOT_URL}/data?n=10`)
      .then((response) => response.json())
      .then((json) => setData(json));
  }, []);

const header = useMemo(() => {
    if(data.length) {
        return getDatatypeKeys(data[0]).map(key => <th>{key}</th>)
    }
}, [data])
  return (
    <div className="data-table">
      <table>
        <thead>
          <tr>
              {header}
          </tr>
        </thead>
        <tbody>
         {data.map((d, idx) => (
            <tr key={idx}>
                {getLine(d)}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DataTable;
