(ns part01.solution
  (:require [clojure.test :refer :all]))

(defn GetInput []
  (map #(Integer/parseInt %) (clojure.string/split-lines (slurp "input")))
)

(defn CalcFuel [mass]
  (- (int (Math/floor (/ mass 3))) 2))

(defn Solution []
  (reduce + (map CalcFuel (GetInput)))
)

(deftest a-test
  (testing "Given examples"
    (is (= (CalcFuel 12) 2))
    (is (= (CalcFuel 14) 2))
    (is (= (CalcFuel 1969) 654))
    (is (= (CalcFuel 100756) 33583))
  )
)

(run-tests)

(print (Solution))