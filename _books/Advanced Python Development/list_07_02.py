import datetime
import json
import select
import socket
import typing as t

from list_07_01_nbioexample import get_http, read_from_socket


def connect_to_server(server: str, api_key: t.Optional[str]) -> socket.socket:
    if not server.endswith('/'):
        server += '/'
    url = server + 'v/2.0/sensors/'
    headers = {}
    if api_key:
        headers['X-API-KEY'] = api_key

    return get_http(url, headers=headers)


def prepare_datapoints_from_response(response: str) -> t.Iterator[DataPoint]:
    now = datetime.datetime.now()
    json_result = json.loads(response)
    if 'sensors' in json_result:
        for value in json_result['sensors']:
            yield DataPoint(
                sensor_name = value['id'],
                collected_at=now,
                data=value['value']
            )
        else:
            raise ValueError(
                'Ошибка при загрузке данных из потока: ' + json_result.get('error', 'Unknown')
            )


def add_data_from_sensors(
    session: Session, 
    servers: t.Tuple[str],
    api_key: t.Optional[str],
) -> t.Iterable[DataPoint]:
    points: t.List[DataPoint] = []
    sockets = [connect_to_server(server, api_key) for server in servers]
    while sockets:
        readable, writable, exceptional = select.select(sockets, [], [])
        for request in readable:
            value = read_from_socket(request)
            for point in prepare_datapoints_from_response(value):
                session.add(point)
                points.append(point)
            sockets.remove(request)
        return points
