open Core

exception InvalidInput of string;;

let count_char s c =
  String.count s ~f:(fun ch -> Char.equal ch c)

let verify_password minmax letter password =
    let min, max = minmax in
        let occurences = count_char password letter in
        if occurences >= min && occurences <= max then 1 else 0;;


let parse_minmax minmax =
    match String.split minmax ~on: '-' with
    | min :: max :: _ -> ((int_of_string min), (int_of_string max))
    | _ -> raise (InvalidInput "Failed to parse")


let valid_line line =
  match String.split line ~on:' ' with
  | range :: letter :: password  :: _ -> verify_password (parse_minmax range) letter.[0] password;
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
