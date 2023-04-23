import { Button, Table, Tag } from "antd";
import { ColumnsType } from "antd/es/table";
import React from "react";

type FlightStatus =
  | "PREFLIGHT"
  | "TAKEOFF"
  | "DEPARTURE"
  | "ENROUTE"
  | "DESCENT"
  | "APPROACH"
  | "LANDING";
type DepartureProcedure = {
  key: string;
  name: string;
  number: string;
  destination: string;
  time: string;
  status: FlightStatus;
};

const DepartureProcedureTable: React.FC = () => {
  const dataSource: DepartureProcedure[] = [
    {
      key: "1",
      name: "JIN AIR",
      number: "LJ121",
      destination: "MACAU (MFM)",
      time: new Date(2023, 3, 23, 22, 5).toLocaleTimeString(),
      status: "PREFLIGHT",
    },
    {
      key: "2",
      name: "KOREAN AIRLINES",
      number: "KE5753",
      destination: "NHA TRANG (CXR)",
      time: new Date(2023, 3, 23, 22, 10).toLocaleTimeString(),
      status: "PREFLIGHT",
    },
  ];

  const columns: ColumnsType<DepartureProcedure> = [
    {
      title: "Flight Name",
      dataIndex: "name",
      key: "name",
    },
    {
      title: "Flight Number",
      dataIndex: "number",
      key: "number",
    },
    {
      title: "Destination",
      dataIndex: "destination",
      key: "destination",
    },
    {
      title: "Time",
      dataIndex: "time",
      key: "time",
    },
    {
      title: "Status",
      dataIndex: "status",
      key: "status",
      render: (text) => {
        return <Tag color="magenta">{text}</Tag>;
      },
    },
    {
      title: "Approval",
      dataIndex: undefined,
      key: "approval",
      render: (_, record) => {
        return <Button>Approve</Button>;
      },
    },
  ];

  return <Table dataSource={dataSource} columns={columns} />;
};

export default DepartureProcedureTable;
