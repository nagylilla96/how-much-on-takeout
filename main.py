from merchants.glovo import fetch_glovo_orders
from merchants.tazz import fetch_tazz_orders
from merchants.presto import fetch_presto_orders

def main():
    total_combined_sum = 0.0
    total_combined_count = 0

    # Fetch Glovo orders
    glovo_total_sum, glovo_order_count = fetch_glovo_orders()
    if glovo_order_count > 0:
        average_order_value_glovo = glovo_total_sum / glovo_order_count
        print(f"Total Glovo sum: {glovo_total_sum:.2f} RON")
        print(f"Total Glovo orders: {glovo_order_count}")
        print(f"Average Glovo order value: {average_order_value_glovo:.2f} RON\n")
        total_combined_sum += glovo_total_sum
        total_combined_count += glovo_order_count

    # Fetch Tazz orders
    tazz_total_sum, tazz_order_count = fetch_tazz_orders()
    if tazz_order_count > 0:
        average_order_value_tazz = tazz_total_sum / tazz_order_count
        print(f"Total Tazz sum: {tazz_total_sum:.2f} Lei")
        print(f"Total Tazz orders: {tazz_order_count}")
        print(f"Average Tazz order value: {average_order_value_tazz:.2f} Lei\n")
        total_combined_sum += tazz_total_sum
        total_combined_count += tazz_order_count

    # Fetch Presto orders
    presto_total_sum, presto_order_count = fetch_presto_orders()
    if presto_order_count > 0:
        average_order_value_presto = presto_total_sum / presto_order_count
        print(f"Total Presto sum: {presto_total_sum:.2f} RON")
        print(f"Total Presto orders: {presto_order_count}")
        print(f"Average Presto order value: {average_order_value_presto:.2f} RON\n")
        total_combined_sum += presto_total_sum
        total_combined_count += presto_order_count

    # Combined totals
    if total_combined_count > 0:
        average_combined_value = total_combined_sum / total_combined_count
        print(f"Combined Total Sum: {total_combined_sum:.2f} RON")
        print(f"Combined Total Orders: {total_combined_count}")
        print(f"Combined Average Order Value: {average_combined_value:.2f} RON")
    else:
        print("No orders data available to calculate combined totals.")

if __name__ == "__main__":
    main()
