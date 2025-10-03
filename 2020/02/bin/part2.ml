open Core

exception InvalidInput of string;;

let indexer s c index =
    Printf.printf "%s %c %d\n" s c index;
    if Char.equal c s.[index] then 1 else 0

let verify_password lohi letter password =
    let len = String.length password in
    let lo, hi = lohi in
    match len with
    | _ when len < lo -> 0
    | _ when len <= hi -> if Char.equal letter password.[lo] then 1 else 0
    | _ -> (indexer password letter lo) lxor (indexer password letter hi)


let parse_lohi lohi =
    match String.split lohi ~on: '-' with
    | lo :: hi :: _ -> ((int_of_string lo) - 1, (int_of_string hi) - 1)
    | _ -> raise (InvalidInput "Failed to parse")


let valid_line line =
    match String.split line ~on:' ' with
  | lohi :: letter :: password  :: _ -> verify_password (parse_lohi lohi) letter.[0] password;
  | _ -> raise (InvalidInput "Failed to parse")


let () =
    let argv = Sys.get_argv () in
    if Array.length argv < 2 then
        eprintf "Usage: %s <filename>\n%!" argv.(0)
    else
        let filename = argv.(1) in
        In_channel.with_file filename ~f:(fun ic -> Printf.printf "%d\n"
        (List.fold_left
            ~init:0
            ~f:(fun acc x -> acc + x)
            (List.map ~f:valid_line (In_channel.input_lines ic))))
;;
