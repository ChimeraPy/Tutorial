import chimerapy as cp

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from chimerapy_tutorial.web_and_screen import VideoNode, ShowWindow


def get_manager(port=9001, logdir="runs"):
    manager = cp.Manager(port=port, logdir=logdir)
    return manager


def get_web_and_screen_pipeline(worker):
    graph = cp.Graph()
    video_node = VideoNode(video_src="../TestData/test1.mp4")
    webcam_node = ShowWindow()
    graph.add_nodes_from([video_node, webcam_node])
    graph.add_edge(video_node, webcam_node)

    mapping = {
        worker.id: [video_node.id, webcam_node.id],
    }

    return graph, mapping


def run_pipeline(pipeline_name: str, **manager_kwargs):
    if pipeline_name not in {"web_and_screen"}:
        raise ValueError(f"Invalid pipeline name: {pipeline_name}")

    manager = get_manager(**manager_kwargs)
    worker = cp.Worker(name="Worker1")
    worker.connect(manager.host, manager.port)
    if pipeline_name == "web_and_screen":
        graph, mapping = get_web_and_screen_pipeline(worker)
        manager.commit_graph(graph, mapping)

    while True:
        q = input("Ready to start? (Y/n)")
        if q.lower() == "y":
            break

    manager.start()

    while True:
        q = input("Stop? (Y/n)")
        if q.lower() == "y":
            break

    manager.stop()
    manager.shutdown()


def run(args=None):
    parser = ArgumentParser(
        "ChimerapyTutorial", formatter_class=ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "pipeline",
        type=str,
        choices=["web_and_screen"],
    )

    parser.add_argument(
        "--manager-port", type=int, default=9001, help="The manager port"
    )

    parser.add_argument(
        "--manager-logdir", type=str, default="runs", help="The manager logdir"
    )

    args = parser.parse_args(args)
    run_pipeline(args.pipeline, port=args.manager_port, logdir=args.manager_logdir)


if __name__ == "__main__":
    run()
