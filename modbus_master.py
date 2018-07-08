
import sys
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
logger = modbus_tk.utils.create_logger("console")
if __name__ == "__main__":
    try:
        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host="127.0.0.1")
        master.set_timeout(5.0)
        logger.info("connected")
        # 读保持寄存器
        logger.info(master.execute(1, cst.READ_COILS, 100, 1))
        logger.info(master.execute(1, cst.WRITE_MULTIPLE_COILS, 100, output_value=[1,0,1,0]))
        
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
