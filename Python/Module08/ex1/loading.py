import importlib.metadata


def ft_check_packages() -> bool:
    requirements = ["pandas", "numpy", "requests", "matplotlib"]

    descricoes = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }

    result = True

    for pack in requirements:
        try:
            __import__(pack)
            version = importlib.metadata.version(pack)
            print(f"[OK] {pack} ({version}) - {descricoes[pack]}")
        except ImportError:
            print(f"[KO] {pack} (Not installed)")
            result = False

    return result


def run_matrix_analysis() -> None:
    """Análise simples com scatter plot"""
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    np.random.seed(42)
    n_samples = 10000

    x = np.random.normal(loc=10, scale=2, size=n_samples)

    print(f"Processing {n_samples} data points...")

    df = pd.DataFrame({
        'Eixo x': x,
    })

    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.hist(
        df['Eixo x'],
        bins=30,
        density=True,
        alpha=0.6,
        color='purple',
        edgecolor='black'
    )

    plt.title(
        'Distribuição Frequencial dos Dados (Curva Normal)',
        fontsize=14,
        fontweight='bold'
    )
    plt.xlabel('Valores Amostrais (Eixo X)')
    plt.ylabel('Densidade de Probabilidade')
    plt.grid(True, alpha=0.3)

    plt.savefig('matrix_analysis.png', dpi=300, bbox_inches='tight')

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    if ft_check_packages():
        run_matrix_analysis()
    else:
        print("\nSome packages are missing.")
        print("\nInstall using pip:")
        print("   pip install -r requirements.txt")
        print("\nOr using Poetry:")
        print("   poetry install")


if __name__ == "__main__":
    main()
