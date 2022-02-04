export type Data = {
  name: string;
  lastname: string;
  age: number;
};

export type SherafObject = {
  id: string;
  _creation: number;
};

export type TodoItem = SherafObject & {
  age: number;
  content: string;
  priority: number;
};
