
let file = "input.txt"

let read_columns file = 
        let ic = open_in file in
        let rec aux left right =
                try
                        let line = input_line ic in
                        let parts = String.split_on_char ' ' (String.trim line)
                                    |> List.filter (fun s -> s <> "")
                        in
                        match parts with
                        | [l; r] -> aux (int_of_string l :: left) (int_of_string r :: right)
                        | _ -> failwith ("Invalid input format: " ^ line)
                with
                | End_of_file ->
                                close_in ic;
                                (List.rev left, List.rev right)
        in
        aux [] []

let take n lst =
        let rec aux i acc = function
                | [] -> List.rev acc
                | x :: xs -> if i < n then aux (i+1) (x :: acc) xs else List.rev acc
        in
        aux 0 [] lst

let sum_distances left right =
        let distances = List.map2 (fun a b -> abs (a - b)) left right in
        List.fold_left (+) 0 distances


let () =
        let (left_column, right_column) = read_columns file in

        let sorted_left = List.sort compare left_column in
        let sorted_right = List.sort compare right_column in
        
        let top_left = take 5 sorted_left in
        let top_right = take 5 sorted_right in
        
        let distances = sum_distances sorted_left sorted_right in

        Printf.printf "Left column: %s\n" (String.concat ", " (List.map string_of_int top_left));
        Printf.printf "Right column: %s\n" (String.concat ", " (List.map string_of_int top_right));

        Printf.printf "Part 1 solution: %s\n" (string_of_int distances);


