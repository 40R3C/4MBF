if __name__ == "__main__":
        try:
                __import__("tes").login()
        except Exception as e:
                exit(str(e))
