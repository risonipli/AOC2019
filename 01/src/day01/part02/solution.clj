(ns day01part02.solution
  (:require [clojure.test :refer :all]))

(defn GetInput []
  (map #(Integer/parseInt %) (clojure.string/split-lines (slurp "input")))
)

(defn CalcFuel [mass]
  (def fuel (- (int (Math/floor (/ mass 3))) 2))
  (if (< fuel 0) 0 fuel)
)

(defn CalcTotalFuel [mass]
  (defn calc [mass acc]
    (if (= mass 0)
      acc
      (calc (CalcFuel mass) (+ (CalcFuel mass) acc))
    )
  )
  (calc mass 0)
)

(defn Solution []
  (reduce + (map CalcTotalFuel (GetInput)))
)

(deftest a-test
  (testing "Given examples"
    (is (= (CalcTotalFuel 14) 2))
    (is (= (CalcTotalFuel 1969) 966))
    (is (= (CalcTotalFuel 100756) 50346))
  )
)

(run-tests)

(print (Solution))