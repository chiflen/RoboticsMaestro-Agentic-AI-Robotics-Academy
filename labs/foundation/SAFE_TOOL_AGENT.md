# Lab F2 — Safe Tool-Using Agent (Mock)
Scenario: a support assistant may look up a synthetic order status, but cannot cancel/refund/change orders.

Build a narrow `lookup_order(order_id)` function; validate IDs; return synthetic data; log tool name/outcome without secrets; handle unknown IDs; test malformed inputs. Stretch: add a human approval step for a mock refund proposal without implementing payments.
